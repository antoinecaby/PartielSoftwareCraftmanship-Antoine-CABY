public class OrderProcessor {

    private Database database;
    private EmailService emailService;
    private InventorySystem inventorySystem;

    // Injection des dépendances plutôt que de les créer directement dans la méthode OrderProcessor
    public OrderProcessor(Database database, EmailService emailService, InventorySystem inventorySystem) {
        this.database = database;
        this.emailService = emailService;
        this.inventorySystem = inventorySystem;
    }

    // Séparation des tâches de la méthodes processOrder en 5 taches différentes
    public void processOrder(Order order) {
        try {
            checkItemAvailability(order);
            saveOrder(order);
            sendConfirmationEmail(order);
            updateInventory(order);
            applyDiscountIfLoyalCustomer(order);
        } catch (ItemNotAvailableException e) {
            System.err.println(e.getMessage());
        }
    }

    private void checkItemAvailability(Order order) throws ItemNotAvailableException {
        List<Item> items = order.getItems();
        for (Item item : items) {
            if (!inventorySystem.isItemAvailable(item)) {
                throw new ItemNotAvailableException("L'item" + item.getName() + " n'est pas dispo dans l'inventaire");
            }
        }
    }

    private void saveOrder(Order order) {
        database.saveOrder(order);
    }

    private void sendConfirmationEmail(Order order) {
        String message = "Votre commande a été reçue et est en cours de traitement.";
        emailService.sendEmail(order.getCustomerEmail(), "Commande confirmé", message);
    }

    private void updateInventory(Order order) {
        for (Item item : order.getItems()) {
            inventorySystem.updateInventory(item, item.getQuantity() * -1);
        }
    }

    private void applyDiscountIfLoyalCustomer(Order order) {
        if (order instanceof LoyalCustomerOrder) {
            LoyalCustomerOrder loyalCustomerOrder = (LoyalCustomerOrder) order;
            loyalCustomerOrder.applyDiscount();
        }
    }
}

class ItemNotAvailableException extends Exception {
    public ItemNotAvailableException(String message) {
        super(message);
    }
}

public class LoyalCustomerOrder extends Order {
    @Override
    public void applyDiscount() {
        setTotalPrice(getTotalPrice() * 0.9); // Appliquer une remise de 10%
    }
}
